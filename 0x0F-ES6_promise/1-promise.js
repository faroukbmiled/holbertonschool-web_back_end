const getFullResponseFromAPI = (success) => {
  return new Promise((resolve, reject) => {
    if (success === true) {
      resolve({
        status: 200,
        body: 'Success'
      });
    } else {
      reject(new Error('The fake API is currently unavailable.'));
    }
  });
};

export default getFullResponseFromAPI;
