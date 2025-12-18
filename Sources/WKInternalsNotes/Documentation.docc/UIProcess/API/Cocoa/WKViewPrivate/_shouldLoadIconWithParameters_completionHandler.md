# ``WKInternalsNotes/WKView/_shouldLoadIconWithParameters(_:completionHandler:)``

リンクアイコン読み込みの可否を決める。

## Objective-C Declaration
```objective-c
- (void)_shouldLoadIconWithParameters:(_WKLinkIconParameters *)parameters completionHandler:(void (^)(void (^)(NSData *)))completionHandler;
```

## Discussion
WKView の実装側に対応メソッドが見当たらない。

## References
- [`WKViewPrivate.h#L151`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKViewPrivate.h#L151)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
