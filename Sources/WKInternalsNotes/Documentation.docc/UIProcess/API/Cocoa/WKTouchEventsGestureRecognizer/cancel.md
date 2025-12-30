# ``WKInternalsNotes/WKTouchEventsGestureRecognizer/cancel()``

現在の状態に応じて recognizer を `Failed` / `Cancelled` に遷移させる。

## Objective-C Declaration
```objective-c
- (void)cancel;
```

## Discussion
状態が `Possible` の場合は `Failed`、`Began` / `Changed` の場合は `Cancelled` に設定する。その他の状態では何もしない。

## References
- [`WKTouchEventsGestureRecognizer.h#L70`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchEventsGestureRecognizer.h#L70)
- [`WKTouchEventsGestureRecognizer.mm#L129`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchEventsGestureRecognizer.mm#L129)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
