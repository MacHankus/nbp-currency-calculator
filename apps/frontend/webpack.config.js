const webpack = require("webpack");
const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");
const dotenv = require("dotenv");
var fs = require("fs");

function fileExists(filePath) {
  try {
    return fs.statSync(filePath).isFile();
  } catch (err) {
    return false;
  }
}


function setUp(mode) {
  console.log(`Available modes are: ['development', 'production']`)
  console.log(`App is building in ${mode}`)
  if (mode === "development" || mode === "develop" || mode === "dev") {
    let devPath = path.resolve(process.cwd(), "develop.env");
    if (fileExists(devPath)) {
      dotenv.config((options = { path: devPath }));
    } else {
      throw Error(`develop.env not exists. Place file in path (${devPath})`);
    }
  } else if (mode === "production" || mode === "prod") {
    let prodPath = path.resolve(process.cwd(), ".env");
    if (fileExists(prodPath)) {
      dotenv.config((options = { path: prodPath }));
    } else {
      throw Error(`.env not exists. Place file in path (${devPath})`);
    }
  }else{
    throw Error(`Mode (${mode}) is unknown.`)
  }
}

module.exports = (env) => {
  // Remember to  use --env mode=.* while building
  setUp(env.mode);

  // return statement
  return {
    mode: "development",
    devtool:"source-map",
    entry: "./main.tsx",
    output: {
      path: path.join(__dirname, "/dist"),
      filename: "bundle.[hash].js"
    },
    devServer: {
      static: path.resolve(__dirname, './dist')
    },
    module: {
      rules: [
        {
          test: [/\.tsx?$/, /\.ts?$/],
          exclude: /node_modules/,
          loader: "ts-loader",
        },
        {
          test: [/\.s[ac]ss$/i, /\.s{0,1}css$/i],
          use: [
            // Creates `style` nodes from JS strings
            "style-loader",
            // Translates CSS into CommonJS
            "css-loader",
            // Compiles Sass to CSS
            "sass-loader",
          ],
        },
      ],
    },
    resolve: {
      extensions: [".jsx", ".tsx", ".js", ".ts"],
    },
    plugins: [
      new HtmlWebpackPlugin({
        template: "./index.html",
        // favicon: "./images/..",
        inject: 'head'
      }),
      new webpack.DefinePlugin({
        "process.env": JSON.stringify(process.env),
      })
    ],
  };
};
