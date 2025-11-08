// frontend/webpack.config.js (The FINAL, Working Configuration)

const path = require('path');

module.exports = {
  // 1. Mode and Paths (Assuming you kept the rest of the file correct)
  mode: 'development',
  // 🛑 Must match the renamed file 🛑
  entry: './src/index.jsx', 
  
  output: {
    filename: 'main.bundle.js', 
    path: path.resolve(__dirname, '..', 'resumesite', 'static', 'resumesite'), 
    publicPath: '/static/', 
  },
  
  module: {
    rules: [
      {
        // 🛑 FIX: Targets files ending in .js OR .jsx 🛑
        test: /\.(js|jsx)$/, 
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            // Include presets directly for maximum reliability
            presets: [
                '@babel/preset-env',
                '@babel/preset-react'
            ]
          }
        }
      },
    ],
  },
  
  // 5. Resolve extensions 
  resolve: {
    extensions: ['.js', '.jsx'],
  },
};