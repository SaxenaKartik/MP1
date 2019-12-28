import React, {Component} from 'react';
import {View, Text, Button} from 'react-native';

export default class AuthLoading extends Component{
    render(){
        return(
            <View>
                <Button
                    title="SignUp"
                />
                <Button
                    title="Login"
                    onPress={() => this.props.navigation.navigate('Login')}
                />
                <Button
                    title="I will login later"
                    onPress={() => this.props.navigation.navigate('Homepage')}
                />
            </View>
        )
    }
}
