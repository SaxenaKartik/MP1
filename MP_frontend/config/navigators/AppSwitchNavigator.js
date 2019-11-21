import { createSwitchNavigator } from "react-navigation";
import AuthLoading from '@screens/authloading';
import {Auth} from './AuthNavigator';
import {AppStack} from './AppNavigator';

export const AppNavigator = createSwitchNavigator({
    AuthLoading: AuthLoading,
    Auth,
    AppStack
},{
    initialRouteName: 'AuthLoading'
});
