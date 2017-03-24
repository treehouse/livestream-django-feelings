var path = require("path");
var webpack = require("webpack");
var BundleTracker = require("webpack-bundle-tracker");

module.exports = {
    context: __dirname,

    entry: [
        'whatwg-fetch',
        'chart.js',
        './feelings/assets/js/index'
    ],

    output: {
        path: path.resolve('./feelings/assets/bundles/'),
        filename: "[name]-[hash].js"
    },

    plugins: [

    ],

    module: {
        loaders: [
            {
                test: /\.jsx?$/,
                exclude: /node_modules/,
                loader: 'babel-loader',
                query: {
                    presets: ['es2015', 'react', 'stage-2']
                }
            }

        ]
    },

    resolve: {
        modules: ['node_modules', 'bower_components'],
        extensions: ['.jsx', '.js'],
        alias: {
            'chart': require.resolve('chart.js')
        }
    }
}