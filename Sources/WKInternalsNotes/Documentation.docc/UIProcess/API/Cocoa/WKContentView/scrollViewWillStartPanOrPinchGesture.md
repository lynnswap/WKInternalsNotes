# ``WKInternalsNotes/WKContentView/scrollViewWillStartPanOrPinchGesture()``

パン/ピンチ開始時の処理を行う。

## Objective-C Declaration
```objective-c
- (void)scrollViewWillStartPanOrPinchGesture;
```

## Discussion
バリデーションメッセージを隠し、キーボードスクロールのアニメータを開始状態にし、ネイティブジェスチャー抑止フラグを無効化する。

## References
- [`WKContentViewInteraction.h#L753`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L753)
- [`WKContentViewInteraction.mm#L4168`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L4168)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
