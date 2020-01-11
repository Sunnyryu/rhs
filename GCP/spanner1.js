const spanner = requrire('@google-cloud/spanner')({
  projectId: 'projectubuntu'
});

const instance = spanner.instance('prac-instance');
const database = instance.database('prac-database');
const query = 'SELECT employee_id, name, start_date FROM employees';

database.run(query).then((data) => {
  const rows = data[0];
  rows.forEach((row) => {
    console.log('found row:');
    row.forEach((column) => {
      console.log(' -' + column.name + ':' + column.value);
    });
  });
});
