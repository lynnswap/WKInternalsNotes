# ``WKInternalsNotes/WKWebExtensionControllerConfiguration/_storageDirectoryPath``

ストレージディレクトリのパスを取得・設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, copy, setter=_setStorageDirectoryPath:) NSString *_storageDirectoryPath;
```

## Default Value
`ENABLE(WK_WEB_EXTENSIONS)` 無効時は `nil`。有効時は `storageDirectory()` が空なら `nil`、それ以外はパス文字列。

## Discussion
getter は `storageDirectory()` が空でなければ `NSString` に変換して返し、setter は `setStorageDirectory(path)` に委譲する。`ENABLE(WK_WEB_EXTENSIONS)` 無効時は `nil` / no-op。

## References
- [`WKWebExtensionControllerConfigurationPrivate.h#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerConfigurationPrivate.h#L51)
- [`WKWebExtensionControllerConfiguration.mm#L198`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerConfiguration.mm#L198)
- [`WKWebExtensionControllerConfiguration.mm#L205`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerConfiguration.mm#L205)
- [`WKWebExtensionControllerConfiguration.mm#L296`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebExtensionControllerConfiguration.mm#L296)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
