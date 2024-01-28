const {defineConfig} = require('@vue/cli-service')
module.exports = defineConfig({
    transpileDependencies: true,
    devServer: {
        headers: {"Access-Control-Allow-Origin": "*"},
        proxy: {
            "^/api": {
                target: "http://127.0.0.1:3000",
                ws: true,
                changeOrigin: true
            }
        }
    }
})
