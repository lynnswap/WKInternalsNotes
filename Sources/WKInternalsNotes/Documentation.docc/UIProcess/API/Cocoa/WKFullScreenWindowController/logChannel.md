# ``WKInternalsNotes/WKFullScreenWindowController/logChannel``

フルスクリーン系ログの出力チャネルを返す。

## Objective-C Declaration
```objective-c
@property (readonly, nonatomic) WTFLogChannel* logChannel;
```

## Default Value
常に `&WebKit2LogFullscreen` を返す。

## Discussion
mac/iOS とも `WebKit2LogFullscreen` のアドレスを返す固定実装で、インスタンス状態には依存しない。

## References
- [`WKFullScreenWindowController.mm#L1100`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/mac/WKFullScreenWindowController.mm#L1100)
- [`WKFullScreenWindowControllerIOS.mm#L2299`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L2299)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
