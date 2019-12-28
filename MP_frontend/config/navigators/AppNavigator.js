import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import Kartik from '@screens/kartik';
import Homepage from '@screens/homepage';

export const AppStack = createStackNavigator({
  Homepage: Homepage,
  Kartik: Kartik,
},
{
  initialRouteName: 'Homepage',
}
);
