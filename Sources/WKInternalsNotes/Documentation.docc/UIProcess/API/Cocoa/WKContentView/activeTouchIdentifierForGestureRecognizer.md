# ``WKInternalsNotes/WKContentView/activeTouchIdentifierForGestureRecognizer(_:)``

指定ジェスチャ認識器に関連付けられたタッチ識別子を返す。

## Objective-C Declaration
```objective-c
- (std::optional<unsigned>)activeTouchIdentifierForGestureRecognizer:(UIGestureRecognizer *)gestureRecognizer;
```

## Discussion
`_touchEventGestureRecognizer` の `activeTouchesByIdentifier` を走査し、該当するタッチがあれば識別子を返す。見つからない場合は `std::nullopt`。

## References
- [`WKContentViewInteraction.h#L775`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.h#L775)
- [`WKContentViewInteraction.mm#L2173`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L2173)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
