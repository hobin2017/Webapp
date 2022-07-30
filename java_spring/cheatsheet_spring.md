# commands
## debug
```bash
mvn package
mvn exec:java -Dexec.mainClass="com.example.restservice.RestServiceApplication"
```
```java
package com.example.restservice;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RestController;
// <dependency>
//   <groupId>org.springframework.boot</groupId>
//   <artifactId>spring-boot-starter-web</artifactId>
// </dependency>
// <dependency>
//   <groupId>org.springframework.boot</groupId>
//   <artifactId>spring-boot-starter-test</artifactId>
//   <scope>test</scope>
// </dependency>

// https://spring.io/quickstart
@SpringBootApplication
@RestController
public class RestServiceApplication {

  @GetMapping("/test")
  public String func01() {
    return "hello world";
  }

  public static void main(String[] args) {
    SpringApplication.run(RestServiceApplication.class, args);
  }
}
```

# http
## http-method
```java
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

@RestController
public class Controller01 {
  // GetMapping is one of the shortcuts of RequestMapping
  @RequestMapping(method=RequestMethod.GET, value="/test")
  public String func01() {
    return "hello world";
  }
}
```
## http-url
### [query-string](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/web/bind/annotation/package-summary.html)
```java
import org.springframework.web.bind.annotation.RequestParam;

@RestController
public class Controller01 {
  @GetMapping("/test")
  public String func01(
    @RequestParam(value = "param01", defaultValue = "") String param01,
    @RequestParam(value = "param02", defaultValue = "") String param02
  ) {
    return " param01: " + param01 + " param02: " + param02;
  }
}
```
### uri parameter
```java
import org.springframework.web.bind.annotation.PathVariable;

@RestController
public class Controller01 {
  @GetMapping("/test/{path01}")
  public String func01(
    @PathVariable String path01
  ) {
    return " path01: " + path01;
  }
}
```
## http-header
```java
import org.springframework.web.bind.annotation.RequestHeader;

@RestController
public class Controller01 {
  @GetMapping("/test")
  public String func01(
    @RequestHeader String header01
  ) {
    return " header01: " + header01;
  }
}
```
## http-body
### raw body
```java
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.ResponseBody;

@RestController
public class Controller01 {
  @GetMapping("/test")
  public @ResponseBody String func01(@RequestBody String rawBody) {
    return rawBody;
  }
}
```
### json
```java
class DataClass01 {
  private String id;

  public String getId(){
    return id;
  }
  public void setId(String id) {
    this.id = id;
  }

  @Override
  public String toString() {  
    return String.format("{id=%s}", id);  
  }
}

@RestController
public class Controller01 {
  @RequestMapping(method=RequestMethod.PUT, value="/test", headers={})
  public String func01(@RequestBody DataClass01 param01) {
    return param01.getClass() + ": " + param01.toString();
  }
}
```
### form
- form-submission 
```java
import org.springframework.web.bind.annotation.ModelAttribute;

class DataClass01 {
  private String id;

  public String getId(){
    return id;
  }
  public void setId(String id) {
    this.id = id;
  }

  @Override
  public String toString() {  
    return String.format("{id=%s}", id);  
  }
}

@RestController
public class Controller01 {
  @RequestMapping(method=RequestMethod.POST, value="/test")
  public String func01(@ModelAttribute DataClass01 param01) {
    return param01.getClass() + ": " + param01.toString();
  }
}
```
- file-upload
```
```
## http-response
### json
```java
@RestController
public class Controller01 {
  @GetMapping("/test")
  public HashMap func01() {
    HashMap map01 = new HashMap();
    map01.put("key01", "value01");
    return map01;
  }
}
```

# code-segments
## router
```java
@RequestMapping(value="/users")  // uri-prefix
@RestController
public class Controller01 {
  @GetMapping("/{id}")
	public String getUserById(@PathVariable String id) {
		return "hello " + id;
	}
}
```
## middleware
## [validate form-input](https://spring.io/guides/gs/validating-form-input/)
```java
import javax.validation.constraints.Size;
import javax.validation.constraints.NotNull;
// <dependency>
//   <groupId>org.springframework.boot</groupId>
//   <artifactId>spring-boot-starter-validation</artifactId>
// </dependency>

class DataClass01 {
  @NotNull
  @Size(min=2, max=30)
  private String id;
}

@RestController
public class Controller01 {
	@RequestMapping(method=RequestMethod.POST, value="/test")
  public String func01(@Valid DataClass02 param01, BindingResult result) {
		if (result.hasErrors()) {
			return "validation-error";
		}
    return param01.getClass() + ": " + param01.toString();
  }
}
```
## [http-request and json-load](https://spring.io/guides/gs/consuming-rest/)

# concepts
