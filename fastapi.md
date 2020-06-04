# FastAPI

## FastAPi初始化流程

| `FastAPI` 继承与 `Starlette`,他主要是封装了一下功能,实际处理请求和响应的还是`Starlette`

### 1.setup函数

| 初始化`FastAPI`时调用的该函数

- 1.添加`opendapi`(Swagger)相关操作,`路由`,`html`,openapi相关的等等.
  
- 2.1 添加了`HTTPException`,`http_exception_handler`, 可以理解为当你程序报错的时候,程序如何返回<br/>
  2.2 添加了`RequestValidationError`,`request_validation_exception_handler` 请求格式正确，但是由于含有语义错误，无法响应(个人理解就是你参数传错了).


| 其余还有初始化了一些内容, `路由`, `默认响应内容`, `openapi的url`

## TODO 其余的下次写把,下班了


