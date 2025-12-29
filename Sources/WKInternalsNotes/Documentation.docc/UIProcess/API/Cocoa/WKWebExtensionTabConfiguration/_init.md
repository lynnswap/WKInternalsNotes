# ``WKInternalsNotes/WKWebExtensionTabConfiguration/_init()``

指定初期化子として `super` の初期化を行う。

## Objective-C Declaration
```objective-c
- (instancetype)_init NS_DESIGNATED_INITIALIZER;
```

## Discussion
内部実装は `return [super init];` のみ。

## References
- [`WKWebExtensionTabConfigurationInternal.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionTabConfigurationInternal.h#L34)
- [`WKWebExtensionTabConfiguration.mm#L35`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionTabConfiguration.mm#L35)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
