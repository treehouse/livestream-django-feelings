var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

var config = require('./webpack.base.config.js');

config.output.path = require('path').resolve('./feelings/assets/dist')

config.plugins = config.plugins.concat([
    new BundleTracker({filename: './feelings/webpack-stats-prod.json'}),

    new webpack.DefinePlugin({
        'process.env': {
            'NODE_ENV': JSON.stringify('production')
        }
    }),

    new webpack.optimize.OccurrenceOrderPlugin(),

    new webpack.optimize.UglifyJsPlugin({
        compressor: {
            warnings: false
        }
    })
])

module.exports = config