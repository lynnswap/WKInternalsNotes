# ``WKInternalsNotes/WKContentView/_disableDoubleTapGesturesDuringTapIfNecessary(_:)``

指定タップに対して必要ならダブルタップを無効化する。

## Objective-C Declaration
```objective-c
- (void)_disableDoubleTapGesturesDuringTapIfNecessary:(WebKit::TapIdentifier)requestID;
```

## Discussion
`requestID` が `_latestTapID` と一致する場合に `_setDoubleTapGesturesEnabled:NO` を呼ぶ。

## References
- [`WKContentViewInteraction.h#L806`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L806)
- [`WKContentViewInteraction.mm#L2699`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2699)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
