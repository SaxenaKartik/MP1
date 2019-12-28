import { createStackNavigator } from "react-navigation-stack";
 import Login from '@screens/authloading/modules/login';
// import ForgotPassword from '@screens/account/modules/authentication/modules/forgot_password';
// import SignUp from '@screens/account/modules/authentication/modules/register';

export const Auth = createStackNavigator({
    Login: Login
},{
    headerMode: 'none',
    initialRouteName: 'Login',
    navigationOptions: {
      headerVisible: false,
    }
});
