# ``WKInternalsNotes/WKFullScreenWindowController/fullScreenViewController``

フルスクリーン表示を担当する `WKFullScreenViewController` を返す。

## Objective-C Declaration
```objective-c
@property (readonly, retain, nonatomic) WKFullScreenViewController *fullScreenViewController;
```

## Default Value
初期値は `nil`。フルスクリーン開始時に生成され、終了時に `nil` へ戻る。

## Discussion
アクセサは `_fullscreenViewController` をそのまま返す。インスタンスは `_enterFullScreen` で生成・設定され、終了や `close` のタイミングで `invalidate` されて破棄される。

## References
- [`WKFullScreenWindowControllerIOS.mm#L914`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L914)
- [`WKFullScreenWindowControllerIOS.mm#L1101`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L1101)
- [`WKFullScreenWindowControllerIOS.mm#L1559`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/fullscreen/WKFullScreenWindowControllerIOS.mm#L1559)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
