# ``WKInternalsNotes/WKContentView/interfaceOrientation``

ウィンドウシーンのインターフェイス方向を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) UIInterfaceOrientation interfaceOrientation;
```

## Default Value
`self.window.windowScene.effectiveGeometry.interfaceOrientation` を返す。

## Discussion
`windowScene` の `effectiveGeometry` から `interfaceOrientation` を取得する。

## References
- [`WKContentView.h#L65`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.h#L65)
- [`WKContentView.mm#L786`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentView.mm#L786)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
