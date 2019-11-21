import React from 'react';
import { createAppContainer } from "react-navigation";
import {AppNavigator} from './navigators/AppSwitchNavigator';


export const AppContainer = createAppContainer(AppNavigator);
