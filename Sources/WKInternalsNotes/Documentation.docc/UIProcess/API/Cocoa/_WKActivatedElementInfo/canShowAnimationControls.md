# ``WKInternalsNotes/_WKActivatedElementInfo/canShowAnimationControls``

アニメーション制御 UI を表示可能かどうかを示す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) BOOL canShowAnimationControls;
```

## Default Value
`NO`（初期化時に設定される）。

## Discussion
iOS では `InteractionInformationAtPosition` の `canShowAnimationControls` を保存し、その値を返す。

## References
- [`_WKActivatedElementInfo.h#L56`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.h#L56)
- [`_WKActivatedElementInfo.mm#L223`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.mm#L223)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
