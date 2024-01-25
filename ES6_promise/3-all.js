import { uploadPhoto, createUser } from './utils';

const handleProfileSignup = async () => {
  try {
    const [photoResp, userResp] = await Promise.all([uploadPhoto(), createUser()]);
    const { body } = photoResp;
    const { firstName, lastName } = userResp;
    console.log(`${body} ${firstName} ${lastName}`);
  } catch {
    console.log('The signup system is currently offline.');
  }
};

export default handleProfileSignup;
