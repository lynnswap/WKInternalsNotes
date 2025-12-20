# ``WKInternalsNotes/_WKDataTask/webView``

タスクが属する `WKWebView` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, weak) WKWebView *webView;
```

## Default Value
`API::DataTask` が page を持たない場合は `nil` を返す。

## Discussion
`API::DataTask::page()` を取得し、存在する場合は `WebPageProxy::cocoaView()` を返す。

## References
- [`_WKDataTask.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDataTask.h#L43)
- [`_WKDataTask.mm#L137`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDataTask.mm#L137)
- [`_WKDataTask.mm#L139`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDataTask.mm#L139)
- [`_WKDataTask.mm#L142`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKDataTask.mm#L142)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
