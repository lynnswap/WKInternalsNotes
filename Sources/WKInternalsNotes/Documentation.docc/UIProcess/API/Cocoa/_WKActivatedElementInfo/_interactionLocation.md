# ``WKInternalsNotes/_WKActivatedElementInfo/_interactionLocation``

ユーザー操作位置の座標を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) WebCore::IntPoint _interactionLocation;
```

## Default Value
`{0, 0}`（初期化時に設定される）。

## Discussion
`InteractionInformationAtPosition` の `request.point` を保持し、その値を返す。

## References
- [`_WKActivatedElementInfoInternal.h#L51`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfoInternal.h#L51)
- [`_WKActivatedElementInfo.mm#L174`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.mm#L174)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
