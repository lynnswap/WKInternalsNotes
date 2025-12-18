# ``WKInternalsNotes/WKWebExtensionControllerConfiguration/_temporaryConfiguration()``

一時ディレクトリを使う永続構成を作成する。

## Objective-C Declaration
```objective-c
+ (instancetype)_temporaryConfiguration;
```

## Discussion
`WebKit::WebExtensionControllerConfiguration::createTemporary()` をラップして返す。`ENABLE(WK_WEB_EXTENSIONS)` 無効時は `nil`。

## References
- [`WKWebExtensionControllerConfigurationPrivate.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerConfigurationPrivate.h#L38)
- [`WKWebExtensionControllerConfiguration.mm#L78`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerConfiguration.mm#L78)
- [`WKWebExtensionControllerConfiguration.mm#L244`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerConfiguration.mm#L244)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
