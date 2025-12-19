# ``WKInternalsNotes/WKContentView/_touchEvent(_:preventsNativeGestures:)``

ネイティブジェスチャー抑止時の内部フラグを更新する。

## Objective-C Declaration
```objective-c
- (void)_touchEvent:(const WebKit::WebTouchEvent&)touchEvent preventsNativeGestures:(BOOL)preventsDefault;
```

## Discussion
抑止対象かつタッチイベント配信中の場合、ロングプレス可否を無効化し、ネイティブジェスチャー抑止フラグと `defaultPrevented` を更新する。

## References
- [`WKContentViewInteraction.h#L790`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L790)
- [`WKContentViewInteraction.mm#L2452`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2452)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
