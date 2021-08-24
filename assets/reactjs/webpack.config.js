const path = require("path");
const webpack = require("webpack");

module.exports = {
  entry: ["./src"],
  output: {
    path: path.resolve(__dirname, "./static/$app_name"),
    filename: "[name].js",
    publicPath: "http://localhost:8080/static/$app_name/",
  },
  module: {
    rules: [
      {
        test: /\.js$$/,
        exclude: /node_modules/,
        use: [
          {
            loader: "babel-loader",
          },
        ],
      },
      {
        test: /\.css$$/,
        exclude: /node_modules/,
        use: [
          {
            loader: "style-loader",
          },
          {
            loader: "css-loader",
          },
        ],
      },
      {
        test: /\.(scss|sass)$$/,
        exclude: /node_modules/,
        use: [
          {
            loader: "style-loader",
          },
          {
            loader: "css-loader",
          },
          {
            loader: "sass-loader",
          }
        ],
      },
      {
        test: /\.(jpe?g|png|gif|svg)$$/,
        use: [
          {
            loader: "file-loader",
          },
        ],
      },
    ],
  },
  optimization: {
    minimize: true,
  },
  devServer: {
    disableHostCheck: true, // does not check for host when using ngrok
    contentBase: "./static/$app_name/",
    headers: {
      "Access-Control-Allow-Origin": "*",
    },
    hot: true,
    inline: true,
    proxy: {
      "!/static/$app_name/**": {
        target: "http://localhost:8000", // points to django dev server
        changeOrigin: true,
      },
    },
  },
  plugins: [
    new webpack.DefinePlugin({
      "process.env": {
        // This has effect on the react lib size
        NODE_ENV: JSON.stringify("production"),
      },
    }),
    // new CompressionPlugin(),
    new webpack.HotModuleReplacementPlugin(),
  ],
};
