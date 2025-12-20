# ``WKInternalsNotes/WKActionSheet/doneWithSheet(_:)``

アクションシートの後処理を行う。

## Objective-C Declaration
```objective-c
- (void)doneWithSheet:(BOOL)dismiss;
```

## Discussion
`dismiss` が `YES` の場合は現在表示中のビューコントローラが自身または回転中に保持したものなら閉じる。内部状態をクリアし、`_currentPresentationStyle` を `WKActionSheetPresentAtTouchLocation` に戻したうえで通知監視を解除する。

## References
- [`WKActionSheet.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.h#L44)
- [`WKActionSheet.mm#L131`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L131)
- [`WKActionSheet.mm#L133`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L133)
- [`WKActionSheet.mm#L139`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L139)
- [`WKActionSheet.mm#L142`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L142)
- [`WKActionSheet.mm#L144`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKActionSheet.mm#L144)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
