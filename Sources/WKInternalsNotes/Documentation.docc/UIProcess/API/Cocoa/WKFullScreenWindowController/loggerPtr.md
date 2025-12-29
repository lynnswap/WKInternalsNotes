# ``WKInternalsNotes/WKFullScreenWindowController/loggerPtr``

ログ出力用の `Logger` を返す。

## Objective-C Declaration
```objective-c
@property (readonly, nonatomic) const Logger* loggerPtr;
```

## Default Value
初期値は `nullptr`。初期化時に `WebPageProxy` の `logger()` を保存する。

## Discussion
`_logger.get()` を返すアクセサで、mac/iOS いずれも初期化時に `WebPageProxy` から取得したロガーを保持する。

## References
- [`WKFullScreenWindowController.mm#L1095`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKFullScreenWindowController.mm#L1095)
- [`WKFullScreenWindowController.mm#L262`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKFullScreenWindowController.mm#L262)
- [`WKFullScreenWindowControllerIOS.mm#L2294`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L2294)
- [`WKFullScreenWindowControllerIOS.mm#L876`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L876)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
