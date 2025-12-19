# ``WKInternalsNotes/WKInspectorViewController/URLForInspectorResource(_:)``

Inspector リソース用の URL を生成する。

## Objective-C Declaration
```objective-c
+ (NSURL * _Nullable)URLForInspectorResource:(NSString *)resource;
```

## Discussion
`WKInspectorResourceScheme` を使って URL を構築し、標準化したパスで返す。

## References
- [`WKInspectorViewController.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorViewController.h#L50)
- [`WKInspectorViewController.mm#L224`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/mac/WKInspectorViewController.mm#L224)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
