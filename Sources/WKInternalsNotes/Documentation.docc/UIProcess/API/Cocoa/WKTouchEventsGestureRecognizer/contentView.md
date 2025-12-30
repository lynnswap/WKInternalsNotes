# ``WKInternalsNotes/WKTouchEventsGestureRecognizer/contentView``

`initWithContentView:` で設定された `WKContentView` を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, weak) WKContentView *contentView;
```

## Default Value
`initWithContentView:` で設定される（それまでは `nil`）。

## Discussion
弱参照のため、`WKContentView` が解放されると `nil` になる。

## References
- [`WKTouchEventsGestureRecognizer.h#L77`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchEventsGestureRecognizer.h#L77)
- [`WKTouchEventsGestureRecognizer.mm#L84`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKTouchEventsGestureRecognizer.mm#L84)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
