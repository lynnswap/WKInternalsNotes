# ``WKInternalsNotes/WKInspectorViewController/delegate``

Inspector View Controller の delegate を設定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, weak) id <WKInspectorViewControllerDelegate> delegate;
```

## Discussion
`_delegate` に弱参照として保持し、必要に応じて Inspector の状態を問い合わせる。

## References
- [`WKInspectorViewController.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorViewController.h#L45)
- [`WKInspectorViewController.mm#L99`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorViewController.mm#L99)
- [`WKInspectorViewController.mm#L133`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorViewController.mm#L133)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
