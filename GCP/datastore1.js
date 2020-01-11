const datastore = require('@google-cloud/datastore')({
  projectId: 'projectubuntu'
});

const itemNames = ['Eggs', 'snack', 'dip', 'celery', 'soju', 'beer'];
const entities = itemNames.map((name) => {
  return {
    key: datastore.key(['todolist', id, 'todoitem']),
    data: {
      name: name,
      completed: False
  }
};
});

datastore.save(entities, (err) => {
  if (err) {
    console.log('error..', err);
  }else{
    entities.forEach((entity) => {
      console.log('created entity', entity.data.name, 'as ID', entity.key.id);
    })
  }
});
