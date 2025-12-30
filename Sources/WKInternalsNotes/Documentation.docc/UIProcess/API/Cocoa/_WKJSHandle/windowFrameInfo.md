# ``WKInternalsNotes/_WKJSHandle/windowFrameInfo(_:)``

ウィンドウフレーム情報を非同期で返す。

## Objective-C Declaration
```objective-c
- (void)windowFrameInfo:(void (^)(WKFrameInfo * _Nullable))completionHandler;
```

## Discussion
`windowProxyFrameIdentifier` から `WebFrameProxy` を取得し、`getFrameInfo` で `WKFrameInfo` を返す。取得できない場合は `nil`。

## References
- [`_WKJSHandle.h#L42`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKJSHandle.h#L42)
- [`_WKJSHandle.mm#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKJSHandle.mm#L56)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
