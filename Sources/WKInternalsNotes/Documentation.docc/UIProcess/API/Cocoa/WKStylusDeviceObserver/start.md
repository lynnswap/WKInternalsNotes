# ``WKInternalsNotes/WKStylusDeviceObserver/start()``

スタイラス状態の監視を開始する。

## Objective-C Declaration
```objective-c
- (void)start;
```

## Discussion
呼び出し回数をカウントし、初回のみ `UIScribbleInteraction.isPencilInputExpected` の KVO 監視を開始する。SDK の挙動フラグが有効な場合にだけ監視を設定する。

## References
- [`WKStylusDeviceObserver.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKStylusDeviceObserver.h#L34)
- [`WKStylusDeviceObserver.mm#L86`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKStylusDeviceObserver.mm#L86)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
