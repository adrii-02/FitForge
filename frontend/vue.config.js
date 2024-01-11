const { defineConfig } = require('@vue/cli-service');

module.exports = defineConfig({
  transpileDependencies: true,

  // Configuración para integración con Django
  outputDir: '../myapp/static/vue', // Cambia 'myapp' por el nombre de tu app de Django
  indexPath: '../../templates/app/index.html', // Cambia 'myapp' por el nombre de tu app de Django

  // Configuración adicional para desarrollo (opcional)
  devServer: {
    proxy: 'http://localhost:8000', // Proxy para el servidor de Django en desarrollo
  },
});