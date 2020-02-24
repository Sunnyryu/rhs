const spanner = requrire('@google-cloud/spanner')({
  projectId: 'projectubuntu'
});

const instance = spanner.instance('prac-instance');
const database = instance.database('prac-database');
const employees = database.table('employees');

employees.insert([
  {employee_id: 1, name: 'dorri', start_date: '1992-01-01'},
  {employee_id: 2, name: 'carycary', start_date: '1988-02-11'}
]).then((data) => {
  console.log('saved data', data);

});
