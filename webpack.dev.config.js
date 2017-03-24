var path = require('path');
var webpack = require('webpack');
var BundleTracker = require('webpack-bundle-tracker');

var config = require('./webpack.base.config.js');

config.entry = config.entry.concat([
    'webpack-dev-server/client?http://localhost:3000',
    'webpack/hot/only-dev-server',
]);

config.output.publicPath = 'http://localhost:3000/assets/bundles/';

config.plugins = config.plugins.concat([
    new webpack.HotModuleReplacementPlugin(),
    new webpack.NoEmitOnErrorsPlugin(),
    new BundleTracker({ filename: './feelings/webpack-stats-dev.json' })
]);

config.module.loaders.unshift(
    {
        test: /\.jsx?$/,
        exclude: /node_modules/,
        loader: 'react-hot-loader'
    }
);

module.exports = config;