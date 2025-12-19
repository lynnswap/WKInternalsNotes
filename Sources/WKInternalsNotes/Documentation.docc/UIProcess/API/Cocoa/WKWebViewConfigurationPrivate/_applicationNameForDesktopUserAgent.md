# ``WKInternalsNotes/WKWebViewConfiguration/_applicationNameForDesktopUserAgent``

Desktop UA 用 application name

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, nullable) NSString *_applicationNameForDesktopUserAgent;
```

## Default Value
iOS: `nil` / macOS: `nil`

## Discussion
- 設定されていない場合: `nil` を返す。
- 設定されている場合: その値を返す。

## References
- [`WKWebViewConfigurationInternal.h#L49`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationInternal.h#L49)
- [`WKWebViewConfiguration.mm#L540`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L540)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
