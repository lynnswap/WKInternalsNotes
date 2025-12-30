# ``WKInternalsNotes/WKDeferringGestureRecognizerDelegate/deferringGestureRecognizer(_:didTransitionToState:)``

ジェスチャの状態遷移に応じて追跡を終了する。

## Objective-C Declaration
```objective-c
- (void)deferringGestureRecognizer:(WKDeferringGestureRecognizer *)deferringGestureRecognizer didTransitionToState:(UIGestureRecognizerState)state;
```

## Discussion
状態が `Ended`/`Failed`/`Cancelled` の場合に `gestureRecognizerConsistencyEnforcer` の追跡を終了する。

## References
- [`WKDeferringGestureRecognizer.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKDeferringGestureRecognizer.h#L40)
- [`WKContentViewInteraction.mm#L10392`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10392)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
