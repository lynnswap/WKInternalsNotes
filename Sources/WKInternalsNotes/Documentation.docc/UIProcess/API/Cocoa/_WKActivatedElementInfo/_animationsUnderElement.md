# ``WKInternalsNotes/_WKActivatedElementInfo/_animationsUnderElement``

要素配下のアニメーション情報（iOS 内部）。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) const Vector<WebCore::ElementAnimationContext>& _animationsUnderElement;
```

## Default Value
空の配列（初期化時に設定される）。

## Discussion
`ACCESSIBILITY_ANIMATION_CONTROL` が有効な場合、`InteractionInformationAtPosition` の `animationsAtPoint` を保存して返す。

## References
- [`_WKActivatedElementInfoInternal.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfoInternal.h#L54)
- [`_WKActivatedElementInfo.mm#L228`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.mm#L228)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
