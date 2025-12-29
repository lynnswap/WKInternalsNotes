# ``WKInternalsNotes/_WKInspectorConfiguration/groupIdentifier``

インスペクター関連ページに付与するグループ識別子。

## Objective-C Declaration
```objective-c
@property (nonatomic, copy, nullable) NSString *groupIdentifier;
```

## Default Value
`nil`。

## Discussion
`applyToWebViewConfiguration:` と `copyWithZone:` で参照され、指定されている場合に `WKWebViewConfiguration` へ反映される。

## References
- [`_WKInspectorConfiguration.h#L61`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorConfiguration.h#L61)
- [`_WKInspectorConfiguration.mm#L90`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKInspectorConfiguration.mm#L90)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
