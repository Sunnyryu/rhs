const datastore = require('@google-cloud/datastore')({
  projectId: 'projectubuntu'
});

const query = datastore.createQuery('Todolist');

datastore.runQuery(query)
  .on('error', console.error)
  .on('data', (entity) => {
    console.log('Found Todolist:\n', entity);
  })
  .on('end', () => {
    console.log('no more todolist');
  });
