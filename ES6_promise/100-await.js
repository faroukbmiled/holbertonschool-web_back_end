import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  try {
    const photoResponse = await uploadPhoto('profile-photo');
    const userResponse = await createUser();
    return { photo: photoResponse, user: userResponse };
  } catch (error) {
    console.error(error);
    return { photo: null, user: null };
  }
}
