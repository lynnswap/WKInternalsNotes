# ``WKInternalsNotes/_WKAutomationSession/configuration``

セッション構成のコピーを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) _WKAutomationSessionConfiguration *configuration;
```

## Default Value
`initWithConfiguration:` に渡した構成のコピーが使われる。

## Discussion
`initWithConfiguration:` で `configuration` をコピーして保持し、getter では都度コピーを返して外部変更から保護する。

## References
- [`_WKAutomationSession.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSession.h#L39)
- [`_WKAutomationSession.mm#L48`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSession.mm#L48)
- [`_WKAutomationSession.mm#L55`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSession.mm#L55)
- [`_WKAutomationSession.mm#L92`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKAutomationSession.mm#L92)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
