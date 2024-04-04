import { resolve as _resolve, join } from 'path'
import HtmlWebpackPlugin from 'html-webpack-plugin'
import { config } from 'dotenv'
import { statSync } from 'fs'

import webpack from 'webpack'

import { fileURLToPath } from 'url';
import { dirname } from 'path';

const __filename = fileURLToPath(import.meta.url);
const __dirname = dirname(__filename);

function fileExists (filePath) {
  try {
    return statSync(filePath).isFile()
  } catch (err) {
    return false
  }
}

function setUp () {
  const devPath = _resolve(process.cwd(), '.env')
  if (fileExists(devPath)) {
    config(({ path: devPath }))
  } else {
    throw Error(`.env not exists. Place file in path (${devPath})`)
  }
}

export default (env) => {
  setUp()

  // return statement
  return {
    mode: 'development',
    devtool: 'source-map',
    entry: './main.tsx',
    output: {
      path: join(__dirname, '/dist'),
      filename: 'bundle.[hash].js'
    },
    devServer: {
      static: _resolve(__dirname, './dist')
    },
    module: {
      rules: [
        {
          test: [/\.tsx?$/, /\.ts?$/],
          exclude: /node_modules/,
          loader: 'ts-loader'
        },
        {
          test: [/\.s[ac]ss$/i, /\.s{0,1}css$/i],
          use: [
            // Creates `style` nodes from JS strings
            'style-loader',
            // Translates CSS into CommonJS
            'css-loader',
            // Compiles Sass to CSS
            'sass-loader'
          ]
        }
      ]
    },
    resolve: {
      extensions: ['.jsx', '.tsx', '.js', '.ts']
    },
    plugins: [
      new HtmlWebpackPlugin({
        template: './index.html',
        // favicon: "./images/..",
        inject: 'head'
      }),
      new webpack.DefinePlugin({
        'process.env.API_PATH': JSON.stringify(process.env.API_PATH)
      })
    ]
  }
}
