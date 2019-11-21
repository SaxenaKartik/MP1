import React, {Component} from 'react';
import {View, Text} from 'react-native';

export default class Login extends Component{
    constructor(props){
        super(props);
        this.state={
            isLoading: true
        }
    }
    componentDidMount(){
        return fetch("http://192.168.43.133:8080/api/user/login/"
        ,{
            method : "POST",
            headers : {
                "User-Agent" : "PostmanRuntime/7.19.0",
                "Accept" : "*/*",
                "Cache-Control" : "no-cache",
                // "Postman-Token" : "5f0e3e7e-8c90-446e-b93c-4248f01c66a5",
                "Postman-Token" : "56b29e44-d37a-4c1f-a3f7-aa3078040f96",
                "Host" : "192.168.43.133:8080",
                "Accept-Encoding" : "gzip, deflate",
                "Content-Type" : "application/json",
                "Content-Length" : "285",
                "Connection" : "keep-alive",
                "cache-control": "no-cache"
            },
            body : JSON.stringify({
                username : 'kartik',
                password : 'scheduler'
            })
        }
    )
      .then(response => response.json())
      .then((responseJson) => {
          console.log(responseJson)
        this.setState({
          isLoading: false,
          dataSource : responseJson.token
        }, function(){}
        );
      })
      .catch((error) =>{
        console.error(error);
      });
    }
    render(){
        return(
            <View>
                <Text>{this.state.dataSource}</Text>
            </View>
        )
    }
}
