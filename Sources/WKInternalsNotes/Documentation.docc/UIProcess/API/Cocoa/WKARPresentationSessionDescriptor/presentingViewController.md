# ``WKInternalsNotes/WKARPresentationSessionDescriptor/presentingViewController``

セッション表示に使うビューコントローラを指定する。

## Objective-C Declaration
```objective-c
@property (nonatomic, nullable, weak, readwrite) UIViewController *presentingViewController;
```

## Default Value
初期値は `nil`。

## Discussion
`_presentingViewController` に保持し、getter で返す。`copyWithZone:` でも引き継がれる。

## References
- [`WKARPresentationSession.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.h#L43)
- [`WKARPresentationSession.mm#L82`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/XR/ios/WKARPresentationSession.mm#L82)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
