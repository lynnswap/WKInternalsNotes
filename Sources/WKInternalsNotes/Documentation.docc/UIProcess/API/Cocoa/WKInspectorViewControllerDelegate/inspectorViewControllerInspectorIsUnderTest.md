# ``WKInternalsNotes/WKInspectorViewControllerDelegate/inspectorViewControllerInspectorIsUnderTest(_:)``

Inspector がテスト中かどうかを返す。

## Objective-C Declaration
```objective-c
- (BOOL)inspectorViewControllerInspectorIsUnderTest:(WKInspectorViewController *)inspectorViewController;
```

## Discussion
`_inspectorProxy` があれば `isUnderTest()` を返し、無ければ `false` を返す。

## References
- [`WKInspectorViewController.h#L59`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorViewController.h#L59)
- [`WebInspectorUIProxyMac.mm#L199`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WebInspectorUIProxyMac.mm#L199)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
