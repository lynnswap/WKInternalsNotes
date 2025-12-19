# ``WKInternalsNotes/WKContentView/_touchEventsRecognized()``

タッチイベントを集約して WebPage に通知する。

## Objective-C Declaration
```objective-c
- (void)_touchEventsRecognized;
```

## Discussion
`_touchEventGestureRecognizer` の最新イベントを取得し、開始イベントでは DOM Paste を拒否しつつアクションシート向けの位置情報更新を行う。`ENABLE(TOUCH_EVENTS)` では `NativeWebTouchEvent` を構築してタッチ操作の抑制可否を反映したうえで `WebPageProxy` に送信し、全タッチ解放時にはデファリング中のジェスチャーや内部フラグをリセットする。

## References
- [`WKContentViewInteraction.h#L1004`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L1004)
- [`WKContentViewInteraction.mm#L2201`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2201)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
