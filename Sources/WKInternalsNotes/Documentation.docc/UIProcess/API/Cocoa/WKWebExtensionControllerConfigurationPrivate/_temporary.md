# ``WKInternalsNotes/WKWebExtensionControllerConfiguration/_temporary``

一時ディレクトリを使う構成かどうかを示す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=_isTemporary) BOOL _temporary;
```

## Default Value
`ENABLE(WK_WEB_EXTENSIONS)` 無効時は `NO`。有効時は `storageIsTemporary()` の結果。

## Discussion
`_webExtensionControllerConfiguration->storageIsTemporary()` を返す。`ENABLE(WK_WEB_EXTENSIONS)` 無効時は `NO`。

## References
- [`WKWebExtensionControllerConfigurationPrivate.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerConfigurationPrivate.h#L38)
- [`WKWebExtensionControllerConfiguration.mm#L78`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerConfiguration.mm#L78)
- [`WKWebExtensionControllerConfiguration.mm#L78`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerConfiguration.mm#L78)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
